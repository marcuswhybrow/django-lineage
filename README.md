Django Lineage
==============

Handling which navigation element is active in a particular template can get a
bit ugly. Often, creating template blocks to drop an  "active" class on a
particular tab or list element.

Lineage makes things neater by defining your conditions once, and it
looks like this:

    {% load lineage %}

    <ul>
        <li {% ifancestor 'home' %}class="active"{% endifancestor %}">
            <a href="{% url 'home' %}">Home</a>
        </li>
        <li {% ifancestor 'blog' %}class="active"{% endifancestor %}">
            <a href="{% url 'blog' %}">Blog</a>
        </li>
        <li {% ifancestor 'about' %}class="active"{% endifancestor %}">
            <a href="{% url 'about' %}">About</a>
        </li>
    </ul>

Whereas before we might have had the following:

`base.html` template:

    <ul>
        <li class="{% block home_class %}{% endblock %}">
            <a href="{% url 'home' %}">Home</a>
        </li>
        <li class="{% block blog_class %}{% endblock %}">
            <a href="{% url 'blog' %}">Blog</a>
        </li>
        <li class="{% block about_class %}{% endblock %}">
            <a href="{% url 'about' %}">About</a>
        </li>
    </ul>

`home.html` template:

    {% extends 'base.html' %}
    {% block home_class %}active{% endblock %}

`blog.html` template:

    {% extends 'base.html' %}
    {% block blog_class %}active{% endblock %}

`about.html` template:

    {% extends 'base.html' %}
    {% block about_class %}active{% endblock %}

Installation
------------

Install using pip:

    pip install django-lineage

Add to INSTALLED_APPS in your Django settings file:

    INSTALLED_APPS = (
        'lineage',
    )

Usage
-----

First, load Lineage's template library:

    {% extends 'base.html'}
    {% load lineage %}

Lineage provides a single template tag `ifancestor` which acts much like the
`if`/`endif` template tag:

    {% ifancestor '/arbitrary/path/' %}
        This content is only displayed if the provided
        path matches the start of the current URL
    {% endifancestor %}

`ifancestor` can also handle a variable:

    {% ifancestor some_variable %}{% endifancestor %}

Or even the same arguments used by the `url` template tag to return an absolute
path given a view function or named pattern.

    {% ifancestor 'core:model_detail' model.pk %}{% endifancestor %}

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
