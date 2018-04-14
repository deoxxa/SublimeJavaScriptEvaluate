import sublime
import sublime_plugin
import subprocess


class JavascriptEvaluateBaseCommand(sublime_plugin.TextCommand):

    def is_visible(self):
        return False


class JavascriptEvaluateSelectionCommand(JavascriptEvaluateBaseCommand):

    def is_visible(self):
        return True

    def run(self, edit):
        sel = self.view.sel()
        for i, r in enumerate(sel):
            text = self.view.substr(r)
            result = subprocess.check_output(['node', '-pe', text])
            self.view.replace(edit, r, result.decode('utf-8').rstrip())
