Django Lineage
==============

Handling which navigation element is active in a particular template can become
annoying. Template blocks can be defined and later overriden to "activate" a
class on a particular navigational element, **but thats gets ugly!**

**Lineage makes things neater** by defining your conditions centrally, and it
looks like this:

    {% load lineage %}

    <ul>
        <li class="{% ancestor '/home/' %}"><a href="/home/">Home</a></li>
        <li class="{% ancestor '/blog/' %}"><a href="/blog/">Blog</a></li>
        <li class="{% ancestor '/about/' %}"><a href="/about/">About</a></li>
    </ul>

When an `ancestor` tag is evaludated, it compares it's argument to the page URL.
If the argument string matches the start of the current pages URL, it outputs
"active". **It's that simple!**

Read on for accepted arguments:

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

The simplest way to use Lineage is the aformentioned `ancestor` tag. Again if
the argument matches the start of the page URL it outputs "active", this should
handle most use cases:

    {% ancestor '/arbitrary/path/' %}

But wait... `ancestor` can also handle variables, filters and all that stuff:

    {% ancestor some_variable|somefilter %}

Or even full blown `url` tag type reverse resolution (Behind the scenes the
`url` tag derives our expected argument - a URL path string.)

    {% ancestor 'core:model_detail' model.pk %}

### Active?

By default `ancestor` outputs "active" if it's argument matches the start of
the page URL. You can globally set the output of the `ancestor` tag by adding
`LINEAGE_ANCESTOR_PHRASE = 'newphrase'` to `settings.py`

### Advanced

If fine-grain control is what your after, you'll be looking for the
`ifancestor/endifancestor` combo:

    {% ifancestor 'pattern_name' %}
        This text here is only renderd if the
        URL argument is an ancestor.
    {% endifancestor %}

It accepts the same exact arguments as `ancestor`, but allows you to define,
on a per definition basis, what the output will be.


Assumptions
-----------

Lineage depends on sensible URL hierarchies, because it compares paths using
regex matching. The `{% ifancestor '/base/' %}` block will be true if the
current URL begins with that URL. For example `/base/` and `/base/section/page/`
return true, but `/other/path/` and `/base` (missing trailing slash) will not.

`request` must be present in the request context, since it's used to determine
the current URL. Django has [a context preprocessor][1] that can insert it for
you.

[1]: https://docs.djangoproject.com/en/dev/ref/templates/api/#django-core-context-processors-request
