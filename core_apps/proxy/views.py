import requests
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.encoding import smart_str

from .forms import SiteForm
from .models import Site, UsageStats


@login_required
def create_site(request):
    """Default function based view with SiteForm object"""
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            new_site = form.save(commit=False)
            new_site.user = request.user
            new_site.save()
            return redirect("dashboard")
    else:
        form = SiteForm()

    return render(request, "proxy/create_site.html", {"form": form})


@login_required
def site_statistics(request, site_id):
    """Function based view with displaying statistics of every added site"""
    site = get_object_or_404(Site, id=site_id, user=request.user)
    stats = UsageStats.objects.get(site=site)
    return render(request, "proxy/site_statistics.html", {"stats": stats})


@login_required
def proxy_site(request, site_name, path=""):
    """Main view with proxied website. First of all we need to parse original site,
    and display it in our way to make proxy thing work
    """
    site = get_object_or_404(Site, user=request.user, name=site_name)
    target_url = f"{site.url}/{path}"

    try:
        # Request to the real site
        response = requests.get(target_url)

        # Updateing statistics
        stats, created = UsageStats.objects.get_or_create(site=site)
        stats.page_visits += 1
        stats.data_received += int(response.headers.get("Content-Length", 0))
        stats.save()

        # content type check
        content_type = response.headers.get("Content-Type", "")

        if "text/html" in content_type:
            # finding all urls and changing it to our own
            soup = BeautifulSoup(response.content, "html.parser")
            for a in soup.find_all("a", href=True):
                href = a["href"]
                if href.startswith("/"):
                    a["href"] = f'/proxy/{site.name}/{href.lstrip("/")}'

            # Change encode type to utf-8 to fix ussues
            content = soup.prettify()
            content_utf8 = smart_str(content, encoding="utf-8")

            return HttpResponse(content_utf8, content_type="text/html; charset=utf-8")

        else:
            # If no html content - sendind  content as it was on original page
            return HttpResponse(response.content, content_type=content_type)

    except requests.exceptions.RequestException:
        return HttpResponseNotFound("Parse error")
