from programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(ruby.is_dynamic())

languages = [ruby, python, visual_basic]
# print(*languages)
# print(languages)
# print(language for language in languages if language.is_dynamic())  # list comprehension does not work
dynamic_languages = [language.name for language in languages if language.is_dynamic()]
print(f"The dynamically typed languages are:")
# print(dynamic_language for dynamic_language in dynamic_languages)  # list comprehension does not work
for dynamic_language in dynamic_languages:
    print(dynamic_language)