init_module:
	git submodule update --init --recursive

pull:
	git fetch --all
	git pull
	git pull origin main --recurse-submodules
	git submodule update --recursive --remote

