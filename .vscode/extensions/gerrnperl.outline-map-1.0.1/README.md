# Outline Map

EN | [中文](https://github.com/Gerrnperl/outline-map/blob/HEAD/README_ZH_CN.md)

![overview](https://github.com/Gerrnperl/outline-map/raw/HEAD/screenshots/overview.png)

A visual, interactive outline map that combines the clarity of the outline with the intuitive overview of the minimap. Enhanced version of vscode built-in outline.

![version](https://img.shields.io/visual-studio-marketplace/v/gerrnperl.outline-map?color=8bf7c7&logo=visualstudio&style=flat-square)
![installs](https://img.shields.io/visual-studio-marketplace/i/gerrnperl.outline-map?color=56b6c2&logo=visualstudiocode&style=flat-square)
![rating](https://img.shields.io/visual-studio-marketplace/stars/gerrnperl.outline-map?color=97dbf3&style=flat-square)


## Features

- ### Automatically scroll, expand and collapse the outline tree
![follow](https://github.com/Gerrnperl/outline-map/raw/HEAD/screenshots/follow.gif)
- ### Navigate through the outline
![navigation](https://github.com/Gerrnperl/outline-map/raw/HEAD/screenshots/nav.gif)
- ### Flag diagnostics
![Flag diagnostics](https://github.com/Gerrnperl/outline-map/raw/HEAD/screenshots/diagnostics.gif)
- ### Search the outline (`<Alt-l>`)
    - `/<exp>`: Normal
    - `=<exp>`: RegExp
    - `?<exp>`: Fuzzy

![Search](https://github.com/Gerrnperl/outline-map/raw/HEAD/screenshots/search.gif)

---

## Configuration
Changes will take effect after restarting the outline view
- `outline-map.color`: color table for specific symbols

- `outline-map.follow`: Scroll the outline when the cursor moves or the viewport scrolls

- `outline-map.hiddenItem`: Choose items you do not want to see in the outline.

- `outline-map.defaultMaxDepth`: Set the default maximum depth of the outline tree. Set this to non-zero to enable the depth button `>` & `<`.

- `outline-map.customFont`: Custom font for the outline. Syntax: `[ <family-name> | <generic-family> ]#`
  
- `outline-map.customCSS`: Custom css for the outline. The css will be injected into the outline's webview.

## Commands
- `outline-map.focusOutline`: Focus outline and start searching or navigating. Default keybinding: `<Alt-l>`

- `outline-map.addDepth` | `outline-map.reduceDepth`: Add / Reduce a level to the outline tree. Only works when `outline-map.defaultMaxDepth` is set to non-zero.
  
- `outline-map.pin` | `outline-map.unpin` | `outline-map.freeze` : Pin / Unpin / Freeze the outline tree.

---

## Suggestion: move view to secondary side panel (vscode ^1.64)
![Initialize settings](https://github.com/Gerrnperl/outline-map/raw/HEAD/images/init.gif)

> Outline Map relies on (vscode || other extensions) to provide symbol information
> 
>  Refer to the following links for more information: [vscode-code-outline/  language-support](https://github.com/patrys/vscode-code-outline#language-support)

---

**Enjoy!**
