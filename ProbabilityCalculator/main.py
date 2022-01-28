from ProbabilityCalculator import Hat, experiment


balls = {"blue":2,"green":1}

hat = Hat(red = 3, blue = 5)



print(experiment(hat, balls, 4, 1000))
