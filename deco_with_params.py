from functools import wraps

FUNCTION_REGISTRY = {}

def register_function(when):

    def subdeco(old_func):
        FUNCTION_REGISTRY[old_func] = when
        return old_func
    
    return subdeco

@register_function("end")
def toast():
    print("toast")

@register_function("start")
def spam():
    print("spam")

@register_function("end")
def ham():
    print("ham")

@register_function("start")
def eggs():
    print("eggs")


for function, when in FUNCTION_REGISTRY.items():
    if when == 'start':
        function()

for function, when in FUNCTION_REGISTRY.items():
    if when == 'end':
        function()