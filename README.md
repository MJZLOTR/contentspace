# contentspace

This project sets up an one-click development environment for Open Telekom Cloud Architecture Center content creators, 
by using [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers). A pre-configured container
environment will be automatically created in Visual Studio Code and accessed as remote container, that has all the necessary
tooling for creating new articles for the Architecture Center.

![devcontainer.png](assets%2Fimages%2Fremote-devcontainer.png)

> [!IMPORTANT]
> Do **not** clone this repo, but instead fork it and clone your fork

## Content

### Submodules

This project is organized with [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules), and that practically
means, that you **should not** import any repository you want to work with by cloning it with `git clone <url>`, **but instead**
importing as a submodule with `git submodule add <url>`.

The project is already pre-linked with the following GitHub repositories as submodules:

- **[opentelekomcloud-docs/architecture-center](https://github.com/opentelekomcloud-docs/architecture-center)**, you are not going to need this, unless you are actively involved in managing the public facing end-product.
- **[opentelekomcloud/otcdocstheme](https://github.com/opentelekomcloud/otcdocstheme)**, you are not going to need it, if you are not actively involved in developing the themes of Help Center or Architecture Center

> [!CAUTION]
> All submodules added in the project, are listed in `.gitmodules`. It is strongly advised not to alter this file manually.

When you clone such a project, by default you get the directories that contain submodules, but none of the files within them yet.
The directoriew are there, but empty. You must run two commands: `git submodule init` to initialize your local configuration file, and `git submodule update` to fetch all the data from that project. Then you need to checkout the branch you want to work with and fetch/merge the changes to your local repos.

### Structure

The newly created or migrated content has always to go under `/doc`. There can be found two sub-folders:

- `/gitea.com`, here should be cloned **only** the repos living in the internal git system 
- `/github.com`, here should be cloned **only** the repos living in any public facing GitHub organization affiliated with Open Telekom Cloud

**Always fork the upstream repos you are going to work with**, unless you instructed otherwise, and add them 
as _submodule_ in one of the aforementioned paths.

> [!IMPORTANT]   
> If you are contributing **new** content, always clone your fork under **gitea.com**, do not create any branch or commits 
> in **opentelekomcloud-docs/architecture-center**.

Under **assets/templates**, you can find a scaffold for two different kind of articles, an external and internal one. All you 
need (if you are contributing new content) is to make a copy of it and fill in the gaps according to the inline instructions.

> [!NOTE]   
> If you are curating migrated content, consult [MIGRATION.md](doc%2Fgitea.com%2FMIGRATION.md)


## Dev Container

Any IDE that supports [Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers), but in this case everything is tailored for Visual Studio Code, will build 
a container with all the necessary prerequisites to get you started creating content immediately based on the extensions 
and features defined in **devcontainer.json**. A `python:1-3.9-bullseye` container will be spawned with the following 
extras pre-installed:

### Visual Studio Code Extensions

- Python, Python Debugger, Python Sphinx Highlighter
- reStructuredText, reStructuredText Syntax Highlighting, Extension Pack for reStructuredText
- Markdown, Markdown All in One, Markdown Preview Enhanced 
- Git Graph
- Resource Monitor
- GraphViz Diagrams Previewer
- Draw.io Integration

### Features

- Git
- tox

### Extras

- GraphViz Diagrams


> [!IMPORTANT]   
> During the provisioning of your container you will be asked to confirm the installation/activation of:
>
> - reStructuredText *docutils* Preview Engine
> - Esbonio Language Server
>
> Click **Yes** to both of them.

### Add your own Extensions

You can add your own extensions in your Dev Container and customize it to the fullest. By right-clicking the desired 
extension in the Marketplace and choosing the "Add to devcontainer.json" the extension will be installed and activated
the next time you rebuild your Dev Container.

![add-extension.png](assets%2Fimages%2Fadd-extension-fs.png)

> [!NOTE]  
> You can afterwards rebuild your container so the changes take effect, with our without using _cache_, in the latter 
> case it will rebuild the container from scratch. 


### Git Credentials

The Git extension will automatically forward your local SSH agent, if one is running otherwise it will use directly the git configuration
of your local host. In that way you can take advantage of keeping tight control of your credentials and your SSH keys in one place, your
local machine, and not spreading them individually to every new development enviroment.

## Using ssh-agent for agent forwarding

There are some cases when you may be cloning your repository using SSH keys instead of a credential helper. To enable this scenario, the extension will automatically forward your **local [SSH agent](https://www.ssh.com/ssh/agent) if one is running**.
Want to know how ssh-agent works? read [SSH Agent Explained](https://smallstep.com/blog/ssh-agent-explained/ "SSH Agent Explained")

You can add your local SSH keys to the agent if it is running by using the `ssh-add` command. Add these lines to your `~/.bash_profile` or `~/.zprofile` (for Zsh) so it starts on login:

```bash
if [ -z "$SSH_AUTH_SOCK" ]; then
   # Check for a currently running instance of the agent
   RUNNING_AGENT="`ps -fp $(pgrep -u $USER) | grep 'ssh-agent -s' | grep -v grep | wc -l | tr -d '[:space:]'`"
   if [ "$RUNNING_AGENT" = "0" ]; then
        # Launch a new instance of the agent
        ssh-agent -s &> $HOME/.ssh/ssh-agent
   fi
   eval `cat $HOME/.ssh/ssh-agent`
fi
```
Open a new shell and test if ssh-agent is runnig by excecuting `ssh-add -l` which shoud list your keys.



### DevPod

You can additionally but not necessarily, fully automate your development lifecycle and provisioning by using the [Open Telekom Cloud provider for Loft Labs' DevPod](https://github.com/akyriako/devpod-provider-opentelekomcloud). DevPod is a a tool, similar to GitHub Codespaces, where you can spawn reproducible developer environments based on the backend of your choice (Azure, AWS, Docker, Kubernetes, Open Telekom Cloud etc) paying only for the machine you are using. Each environment is an isolated instance running in a container whose image is specified in **devcontainer.json**, as we discussed already. 

![devpod.png](assets%2Fimages%2Fdevpod.png)





