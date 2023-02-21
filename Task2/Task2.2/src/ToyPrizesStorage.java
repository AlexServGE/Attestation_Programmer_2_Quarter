import java.util.LinkedList;
import java.util.Queue;

public class ToyPrizesStorage {
    protected Queue<Toy> prizesStorage;

    public ToyPrizesStorage() {
        this.prizesStorage = new LinkedList<>();
    }

    public void addToy(Toy someToy) {
        this.prizesStorage.add(someToy);
    }

    public void deleteToy() {
        this.prizesStorage.poll();
    }

    public Toy getNextToy(){
        return this.prizesStorage.peek();
    }

    public Queue<Toy> getPrizesStorage() {
        return prizesStorage;
    }

    @Override
    public String toString() {
        return "ToyPrizesStorage{" +
                "prizesStorage=" + prizesStorage +
                '}';
    }
}
