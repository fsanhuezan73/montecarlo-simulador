FROM 235494787662.dkr.ecr.us-east-1.amazonaws.com/montecarlo-app:latest
EXPOSE 5001
CMD ["python", "app.py"]
