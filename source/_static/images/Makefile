svg:
	for file in *.pdf; do \
		name=`basename "$$file" .pdf`; \
		inkscape -z -l="$$name.svg" "$$name.pdf"; \
	done


clean:
	rm *.svg
