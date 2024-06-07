@echo off
if [%1] == [] GOTO help
zip -urvop9 dist\analizzatore_smf_123_2_sorgenti_%1.zip .vscode\* data_layer\* doc_analizzatore_smf\* .gitignore estrattore.py ipython_loc.cmd measure_time.ps1 Pipfile Pipfile.lock analizzatore_smf_123_2.py README.md measure_time.ps1 build_dist.cmd
pyinstaller analizzatore_smf_123_2.py --noconfirm
zip -urvop9 dist\analizzatore_smf_123_2_%1.zip dist\analizzatore_smf_123_2\*
GOTO end

:help
@echo.
@echo "Utilizzo: build_dist <numero di versione>"
@echo "Il numero di versione e` una stringa del tipo: x.y.z"
@echo.
@echo "Esempio : build_dist 1.3.33"

:end
@echo on