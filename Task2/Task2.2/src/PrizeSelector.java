import java.util.Map;
import java.util.Random;

public class PrizeSelector {

    /*
    содержит очередь призов
    может случайно выбирать одну из игрушек в зависимости от веса игрушки
    может добавлять одну из игрушек в очередь на выдачу
     */

    public void selectToyToBePrize(ToyStorage someToyStorage, ToyPrizesStorage somePrizesStorage) {
        Random rnd = new Random();
        int rndNumber = rnd.nextInt(101);
        int winnerCursor = someToyStorage.getTotalToyWeight() / 100 * rndNumber;
        int searchCursor = 0;
        Map<Integer, Toy> toyStorage = someToyStorage.getToyStorage();
        for (Integer item : toyStorage.keySet()) {
            searchCursor += toyStorage.get(item).getWeight();
            if (searchCursor > winnerCursor) {
                Toy winnerToy = toyStorage.get(item);
                System.out.printf("В конкурсе выиграла игрушка - %s \n", winnerToy);
                somePrizesStorage.addToy(winnerToy);
                System.out.printf("Она добавляется в массив призов - %s \n", somePrizesStorage);
                someToyStorage.deleteToy(item);
                System.out.printf("На складе игрушек остались следующие игрушки - %s \n", someToyStorage);
                break;
            }
        }
    }

}
