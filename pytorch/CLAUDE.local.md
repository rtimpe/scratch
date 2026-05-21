# Environment

The development environment in ~/git/pytorch is managed by pixi and is called `py314`.  Use `pixi s -e py314` to open a shell in the correct environment.  The pixi environment is defined in `~/git/torch-build`.  Pixi commands need to be run from there.  Do not make changes to that directory.  In ~/git/pytorch-313 the environment is `py313`

The environment for ~/git/pytorch-315 is slightly different.  It uses a local (debug) build of cpython.  The cpython source source code is at ~/git/cpython.  The pixi env name is `cpython`
