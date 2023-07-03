


all:
ifneq ($(wildcard ~/obj_orie_prog_app/.*),)
	cd obj_orie_prog_app
endif

	git add .
	git commit -m "$(message)"
	git push -u origin