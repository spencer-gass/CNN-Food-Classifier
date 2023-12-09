from trainers import food_or_not_trainer
from trainers import food_101_trainer
from trainers import good_for_lunch_trainer
from trainers import good_for_dinner_trainer
from trainers import good_for_lunch_or_dinner_trainer
from attributeModelEvaluator import goodForLunchModelEvaluator

if __name__ == '__main__':
    print()
    # food_or_not_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False)
    # food_101_trainer(lr=1e-3, epochs=10, batch_size=20, continue_training=False)
    # good_for_dinner_trainer(lr=1e-4, epochs=80, batch_size=20, continue_training=True)
    # good_for_lunch_trainer(lr=1e-4, epochs=40, batch_size=20, continue_training=True)
    good_for_lunch_or_dinner_trainer(lr=1e-4, epochs=20, batch_size=20, continue_training=True)
    # goodForLunchModelEvaluator()
