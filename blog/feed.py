from django.contrib.syndication.views import Feed
from .models import Entry


class LatestPosts(Feed):
    title = "My blog"
    link = "/feed/"
    description = "Latest Posts of Mine"

    def items(self):
        return Entry.object.published()[:5]