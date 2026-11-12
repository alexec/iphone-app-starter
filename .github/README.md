# iPhone app starter

A template for a new iPhone app in SwiftUI: TestFlight on each version tag, then the App
Store when a person approves it, with Xcode's cloud-managed signing and Sentry for crashes.
The app's own README is [README.md](../README.md): it is what a new app gets.

[Agents](https://github.com/alexec/Agents) makes a new app's repository from it with its
`make_app_repository` tool (starter `iphone-app`, or this repository by name). You can also
press **Use this template**, then fill the placeholders yourself.

## Placeholders

Each file names what the person chose with a placeholder. Agents fills them before the first
commit, so a new app never says one.

| Placeholder | What | Example |
| --- | --- | --- |
| `__APP_NAME__` | the app's name, as the person says it | `Tide Log` |
| `__BUNDLE_ID__` | the app's bundle id | `com.example.tidelog` |

## The template's own files

`.starterignore` names the files that are this template's, not the app's: this README, its
CI (`.github/workflows/template.yml`) and `.github/template/`. Agents leaves them out of a
new app. The CI fills the placeholders with sample values (`.github/template/fill.py`),
checks the workflows and builds the app for the simulator, so a change here is checked here.

To make your own starter, fork this repository, change it and name your fork as the starter.
Agents takes the default branch each time, so a fix reaches the next new app at once.
