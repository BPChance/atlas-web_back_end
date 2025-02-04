import gettext
from babel import Locale


# set up translation functions
_ = gettext.gettext
ngettext = gettext.ngettext

# mark str's for translation
greeting = _("Hello, World!")
num = 3
message = ngettext("You have one message", "You have %(num)d messages", num) % {"num": num}

print(greeting)
print(message)
