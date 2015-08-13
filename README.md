Django Lineage
==============

Which navigation element is "active" in a template? Lineage determines a navigation element's state by inspecting the page URL:

    {% load lineage %}

    <ul>
        <li class="{% ancestor '/home/' %}"><a href="/home/">Home</a></li>
        <li class="{% ancestor '/blog/' %}"><a href="/blog/">Blog</a></li>
        <li class="{% ancestor '/about/' %}"><a href="/about/">About</a></li>
    </ul>

If the argument of `ancestor` matches the start of the URL (e.g. this nav element is at least a parent of this page), it outputs "active". **It's that simple!**

Installation
------------

Install using pip:

    pip install django-lineage

Add `'lineage'` to `INSTALLED_APPS` in `settings.py`:

    INSTALLED_APPS = (
        'lineage',
    )

Usage
-----

The `ancestor` tag needs to, of course, be loaded into your template:

    {% load lineage %}

The first way to use Lineage is the aformentioned `ancestor` tag. Again if the argument matches the start of the page URL it outputs "active", this should handle most use cases:

    {% ancestor '/arbitrary/path/' %}

`ancestor` can also handle variables, filters and all that stuff:

    {% ancestor some_variable|somefilter %}

Most importantly it also accepts `url` tag type reverse resolution (Behind the scenes the `url` tag derives our expected argument - a URL path string.)

    {% ancestor 'core:model_detail' model.pk %}

### Output Defaults to "active"

By default `ancestor` outputs "active" on a match. You can alter this default by adding `LINEAGE_ANCESTOR_PHRASE = 'newphrase'` to `settings.py`

### Overring Output

Override output on demand using the `ifancestor/endifancestor` combo:

    {% ifancestor 'pattern_name' %}
        This text here is only renderd if the
        URL argument is an ancestor.
    {% endifancestor %}


Assumptions
-----------

Lineage depends on sensible URL hierarchies, because it compares paths using regex matching. `{% ancestor '/base/' %}` will fire if the current URL begins with `/base/`. For example `/base/` and `/base/section/page/` return true, but `/other/path/` and `/base` (missing trailing slash) will not.

`request` must be present in the request context, since it's used to determine the current URL. Django has [a context preprocessor][1] that can insert it for you.

[1]: https://docs.djangoproject.com/en/dev/ref/templates/api/#django-core-context-processors-request


Similar Alternatives
--------------------

* [Django Menus][django-menus]

[django-menus]: https://bitbucket.org/schinckel/django-menus/overview
