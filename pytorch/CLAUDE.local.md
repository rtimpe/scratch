# Environment

Development environments are managed by pixi, and are defined in `~/git/torch-build`.  Do not make changes to that directory.  See the below table for a mapping of directory to environment name

| Directory | env name |
|-|-|
| ~/git/pytorch | py314 |
| ~/git/pytorch-315 | py315 |
| ~/git/pytorch-313 | py313 |

There is also a `cpython` environment (currently unused) for development versions of cpython.  Use the `~/git/cpython` directory to read cpython source code, but do not make changes.

`gh` is not installed.  Don't attempt to write to github.  You don't have permissions to perform `git fetch` - ask me if this is needed.

# Code reviews
Building pytorch is slow - be careful not to make changes to C/C++ files unless necessary.  When doing code reviews, prefer cherry picking changes vs checking out commits (which are often on a different base commit, and would need a rebuild)

# Other

Don't try to run linters unless explicitly asked to.
