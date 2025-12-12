!!! info "Information:"
    Something **new** is coming to `mkdocs-shadcn`

!!! note "Note:"
    We notice that `x=2`

!!! warning "Warning:"
    There is a *risk* doing `x/0`

!!! danger "Danger:"
    Don't look at `node_modules` **please**!

!!! note "Admonition + Code"
    You may face the limits of `codehilite` however.

        :::python
        def fibonacci(n):
            a, b = 0, 1
            for _ in range(n):
                yield a
                a, b = b, a + b

        for num in fibonacci(10):
            print(num)

[Reference](https://python-markdown.github.io/extensions/attr_list/){: class="reference" }

    :::python
    import numpy as np # просьба нажимать таб для развития



хехеххехехехе


/// codexec

    :::python
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    for num in fibonacci(10):
        print(num)

///

### FAQ

/// details | Is this theme an official shadcn port?
No. But you can still [star it +heroicons:star+](hhttps://github.com/asiffer/mkdocs-shadcn)
///


/// details | Why a new mkdocs theme while `material` exists?
First the [shadcn/ui](https://ui.shadcn.com/) theme is just incredible. 

Actually, nothing can compete with the [material](https://squidfunk.github.io/mkdocs-material/) theme which is very mature and feature rich. 

In addition to sticking to the shadcn theme, the idea is to remain a simple theme, providing some special built-in features that we may not find in other themes.
///


/// details | Is it open to contributions?
Yes, yes and yes! On its own, the theme tries to provide more and more relevant extensions/plugins. But anyone can define what could be relevant! 

[Open an issue](https://github.com/asiffer/mkdocs-shadcn/issues) and let us discuss about it +heroicons:face-smile+
///

/// details | Is `mkdocs-rube-goldberg-plugin-extension` supported?
In general no.
///
