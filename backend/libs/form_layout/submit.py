from crispy_tailwind.layout import Submit as TailwindSubmit


class Submit(TailwindSubmit):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault(
            "css_class",
            # "bg-cyan-500 hover:bg-cyan-700 text-white font-bold py-2 px-4 rounded",
            # "flex w-full justify-center rounded-md bg-cyan-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-cyan-700"
            "flex w-full justify-center rounded-md bg-cyan-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-cyan-600",
        )
        super().__init__(*args, **kwargs)
