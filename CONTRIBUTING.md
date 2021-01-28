## Getting Started

To avoid having to configure and manage dependencies and virtual environments between different dev and release machines, development/test/release builds are done inside a Docker container. Contributors do not even need to have a Python installation on their machine. This approach is not required - a contributor can choose to install the dependencies on their own machine and develop from there - but it is encouraged as it integrates nicely with the anticipated build/deploy/release model of the final program.

*Assumptions:*
- Git is installed
- Basic understanding of shell navigation

#### 1. Install Docker

##### Linux
[Install Docker Engine](https://docs.docker.com/engine/install/)

Make sure the current user gets added to the `docker` group as per the instructions [here](https://docs.docker.com/engine/install/linux-postinstall/).

##### Windows
[Install Docker Desktop on Windows](https://docs.docker.com/docker-for-windows/install/)

##### Mac
[Install Docker Desktop on Mac](https://docs.docker.com/docker-for-mac/install/)

> ***Note***
> *If you are not familiar with Docker, there are some good introductory tutorials available [here](https://docs.docker.com/get-started/).*
> *The basic tutorial is quick and gives almost all of the information required to contribute to this project via Docker.*

#### 2. Clone git repository

Ensure git is installed, then run:
```shell
git clone https://github.com/jdrempel/atmos.git
```

#### 3. Configure development environment
##### Option 1: Remote into Docker container (Preferred)

> ***Note***
> *The instructions here assume the use of **Microsoft Visual Studio Code** (aka VS Code).*
> *Using a different editor for the same purpose may work but is not covered here.*

1. Ensure the `Remote - Containers` extension is installed in VS Code.
2. Open the project's base directory in the editor.
3. In the command palette, select `Remote-Containers: Reopen in Container`.
4. A new window opens in the virtual environment within the Docker container. It may take several minutes to load the first time as Docker downloads the required components and then builds the image. This environment contains all necessary dependencies for the project so nothing else needs to be installed or reconfigured on the local (host) machine.

##### Option 2: Develop on host machine

This method is not the "officially recommended" approach as it will involve setting up and subsequently maintaining dependencies in the local dev environment. That being said, it is a perfectly viable alternative.

Here are the primary considerations:

- It is a good idea to create and manage a Python virtual environment to avoid conflicting versions of Python and/or packages between the local machine's "main" Python installation and the project's needs.
- After `git fetch` or `git pull`, be sure to check for any changes or additions to `requirements.txt`. If there are any, run `pip install -r requirements.txt` to update the installed packages accordingly.

#### Appendix A - Manually override Docker image build

While remote tools should automatically build and run the Docker image, there are also scripts for managing this in a Mac or Linux shell, or it can be done manually using `docker build` on the command-line. On Windows it is probably best to use PowerShell or the Docker Desktop GUI. WSL is another option (YMMV).

##### Linux/Mac

Either:
```shell
bash build.sh atmos
```
...or:
```shell
chmod +x build.sh
./build.sh atmos
```

##### Windows (or manual)

```shell
docker build --target atmos -t atmos
```
