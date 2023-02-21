public class Toy {

    /*
    содержит атрибуты игрушки
    может изменять некоторые атрибуты через сеттер

    id игрушки,
текстовое название,
количество
частота выпадения игрушки (вес в % от 100)
     */

    protected static int id = 1;
    protected int toyId;
    protected String title;
    protected int weight;

    public Toy(String title, int weight) {
        this.toyId = id++;
        this.title = title;
        this.weight = weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }


    public int getToyId() {
        return toyId;
    }

    public String getTitle() {
        return title;
    }

    public int getWeight() {
        return weight;
    }

    @Override
    public String toString() {
        return "Toy{" +
                "toyId=" + toyId +
                ", title='" + title + '\'' +
                ", weight=" + weight +
                '}';
    }
}
