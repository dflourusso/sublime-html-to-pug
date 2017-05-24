import os
import sublime
import sublime_plugin

class HtmlToPugFromFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    source = self.view.file_name()
    if source.endswith(".html"):
      target = source + '.pug'
    if target:
      Pug.convert(source, target)
      self.view.window().open_file(target)

  def is_enabled(self):
    return True #return (self.view.file_name().endswith(".html") or self.view.file_name().endswith(".erb"))

class HtmlToPugFromSelectionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        html = self.view.substr(region)
        pug = Pug.buffer(html)
        if pug != None:
          self.view.replace(edit, region, pug)

  def is_enabled(self):
    return True #return self.view.file_name().endswith(".pug")

class HtmlToPugFromClipboardCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    html = sublime.get_clipboard()
    pug = Pug.buffer(html)
    if pug != None:
      for region in self.view.sel():
        self.view.replace(edit, region, pug)

  def is_enabled(self):
    return True #return self.view.file_name().endswith(".pug")

class Pug:
  @classmethod
  def convert(self, html_file, pug_file):
    cmd = ' '.join(['/usr/local/bin/html2jade', '--noemptypipe', '--bodyless', html_file, pug_file])
    from subprocess import call
    call(cmd, shell=True)
    return True

  @classmethod
  def buffer(self, html):
    html_file = "/tmp/_sublime_buffer.html"
    pug_file = "/tmp/_sublime_buffer.jade"

    with open(html_file, "w") as tmp_file:
      tmp_file.write(html)

    self.convert(html_file, pug_file)
    pug = open(pug_file, 'r').read()

    os.remove(html_file)
    os.remove(pug_file)

    return pug
