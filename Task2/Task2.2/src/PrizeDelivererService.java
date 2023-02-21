import java.io.FileWriter;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class PrizeDelivererService {

    public void deliverPrize(ToyPrizesStorage somePrizesStorage) throws IOException {
        Toy nextPrizeToDeliver = somePrizesStorage.getNextToy();
        somePrizesStorage.deleteToy();
        Logger lg = Logger.getLogger(getClass().getName());
        try (FileWriter fw = new FileWriter("toysDelivered.txt", true)){
            fw.append(nextPrizeToDeliver.toString());
        } catch (IOException e){
            lg.log(Level.WARNING,"Ошибка в момент записи данных в файл. Провал записи в файл.");
            throw e;
        }
    }
}
