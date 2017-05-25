# HTML to PUG plugin for Sublime Text 3

Converts files, selection and clipboard content from HTML to PUG using html2jade

## Installation

Install *html2jade*:

    $ yarn global add html2jade
    $ ln -s $(which html2jade) /usr/local/bin/html2jade

### [Sublime Package Decontrol](https://github.com/jfromaniello/Sublime-Package-Decontrol)

- Install package decontrol
- Type `command+shift+p`
- Enter project url `dflourusso/sublime-html-to-pug`
In the command Pallette choose **Package Control: Install Repository** and select **HtmlToPug**

### Git installation

Clone the repository in your Sublime Text "Packages" directory:

    $ git clone https://github.com/dflourusso/sublime-html-to-pug.git HtmlToPug


The "Packages" directory is located at:

* OS X:

    ~/Library/Application\ Support/Sublime\ Text\ 3/Packages

* Linux:

    ~/.config/sublime-text-3/Packages/


### Uninstall

Remove the folder in `~/Library/Application\ Support/Sublime\ Text\ 3/Packages/<HtmlToPugFolder>`

## Usage

* **Convert selection** `Shift+Alt+S` - replaces selection of HTML with PUG content.
* **Convert clipboard content** `Shift+Alt+V` - inserts PUG of converted clipboard HTML content.

### In Command Palette:

* **HtmlToPug: Convert selection**
* **HtmlToPug: Convert clipboard content**

