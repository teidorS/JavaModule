public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        int carsPerSpeed = 221;
        if (speed <= 4) {
            return speed * carsPerSpeed;
        } else if (speed <= 8) {
            return (speed * carsPerSpeed) - (0.1 * speed * carsPerSpeed);
        } else if (speed == 9) {
            return (speed * carsPerSpeed) - (0.2 * speed * carsPerSpeed);
        } else {
            return (speed * carsPerSpeed) - (0.23 * speed * carsPerSpeed);
        }
    }

    public int workingItemsPerMinute(int speed) {

        int carsPerSpeed = 221;
        double carsPerMinute = carsPerSpeed / 60.0;
        if (speed <= 4) {
            return (int)(speed * carsPerMinute);
            
        } else if (speed <= 8) {
            return (int) ((speed * carsPerMinute) -  (0.1 * speed * carsPerMinute));
        } else if (speed == 9) {
            return (int) ((speed * carsPerMinute) -  (0.2 * speed * carsPerMinute));
        } else {
            return (int) ((speed * carsPerMinute) - (0.23 * speed * carsPerMinute));
        }
    }
}
