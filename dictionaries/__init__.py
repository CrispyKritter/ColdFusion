import sublime
import sublime_plugin

# scopes in which to trigger cfml tags auto complete
CFML_TAG_SCOPE = 'text.html.cfm -source -meta -comment, text.html.cfm source.js -meta -comment, meta.scope.between-output-tags.cfml -comment, text.html.cfm.embedded -source.cfscript.embedded -meta -comment'
# scopes in which to trigger cfml tag attributes auto complete
CFML_TAG_ATTRIBUTE_SCOPE = 'meta.tag.inline.cf -string, meta.tag.block.cf -string'
# scopes in which to trigger cfscript functions auto complete
CFSCRIPT_FUNCTION_SCOPE = 'source.cfscript -meta.function -meta.function-call -variable.other.dot -variable.other.local -string -comment'
# scopes in which to trigger function call parameters auto complete
CFSCRIPT_FUNCTION_ARGS_SCOPE = 'meta.function-call.cfscript -string -comment'
# scopes in which to trigger tag operator arguments
CFSCRIPT_TAGOPERATOR_ATTRIBUTE_SCOPE = 'meta.operator -string -comment'
# scopes in which to trigger variable completions
CFSCRIPT_VARIABLES_SCOPE = 'variable.other.dot.cfscript'
# scopes that trigger auto complete on spacebar key press // meta.tag.inline.cf.other excludes cfset/cfreturn
AC_ON_SPACE_SCOPE = 'meta.function-call.cfscript -meta.tag.inline.cf.other, meta.tag -meta.tag.inline.cf.other, meta.operator'
# scopes that trigger on dot auto completions
AC_ON_DOT_SCOPE = 'source.cfscript'

def get_tag_name(view, start_pt):
    return get_tag_info(view, start_pt)[0]

def get_tag_attribs(view, start_pt):
    return get_tag_info(view, start_pt)

# *****************************************************************************************
# HELPERS 
# *****************************************************************************************
def get_tag_info(view, start_pt):
    taginfo = view.substr(sublime.Region(0, start_pt)).split("<").pop().split(" ")
    return taginfo