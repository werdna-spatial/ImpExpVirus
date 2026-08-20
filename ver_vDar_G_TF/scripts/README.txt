sbatch --job-name=m64HOOH ./SCR_8x8.sbatch

sbatch --job-name=NC_npzd --export=RUN_DIR=/lustre/isaac24/scratch/ecarr/runs/run_25vDar_G_UTK_tempfunV2_4327674,MODEL_RUNID=4327674 ./scripts/NC_createTracer.sbatch

