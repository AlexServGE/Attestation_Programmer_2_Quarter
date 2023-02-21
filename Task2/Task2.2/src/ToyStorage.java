import java.util.HashMap;
import java.util.Map;

public class ToyStorage {
    /*
    содержит игрушки
    может принимать в себя и удалять из себя игрушки

    имеет два экземпляра
    на хранение обычных игрушек
    на хранение призов

     */

    protected Map<Integer, Toy> toyStorage;
    protected int totalToyWeight;

    public ToyStorage() {
        this.toyStorage = new HashMap<>();
        this.totalToyWeight = 0;
    }

    public void addToy(Toy someToy) {
        this.toyStorage.put(someToy.getToyId(), someToy);
        this.totalToyWeight += someToy.getWeight();
    }

    public void deleteToy(Integer someToyId) {
        this.totalToyWeight -= toyStorage.get(someToyId).getWeight();
        this.toyStorage.remove(someToyId);
    }


    public int getTotalToyWeight() {
        return totalToyWeight;
    }

    public Map<Integer, Toy> getToyStorage() {
        return toyStorage;
    }

    @Override
    public String toString() {
        return "ToyStorage{" +
                "toyStorage=" + toyStorage +
                '}';
    }
}
