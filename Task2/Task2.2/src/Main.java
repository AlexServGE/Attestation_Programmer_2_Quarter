import java.io.IOException;

public class Main {
    public static void main(String[] args) {

        Toy toy1 = new Toy("Lego", 10000);
        Toy toy2 = new Toy("Doll", 10000);
        Toy toy3 = new Toy("Car", 1);
        Toy toy4 = new Toy("Game", 1);

        ToyStorage taskToyStorage = new ToyStorage();

        taskToyStorage.addToy(toy1);
        taskToyStorage.addToy(toy2);
        taskToyStorage.addToy(toy3);
        taskToyStorage.addToy(toy4);

        ToyPrizesStorage taskPrizesStorage = new ToyPrizesStorage();
        PrizeSelector selector = new PrizeSelector();



        selector.selectToyToBePrize(taskToyStorage, taskPrizesStorage);
        selector.selectToyToBePrize(taskToyStorage, taskPrizesStorage);
        selector.selectToyToBePrize(taskToyStorage, taskPrizesStorage);


        PrizeDelivererService deliverer = new PrizeDelivererService();

        try {
            deliverer.deliverPrize(taskPrizesStorage);
        } catch (IOException e) {
            System.out.println("Не удалось записать в файл");
        }
    }
}