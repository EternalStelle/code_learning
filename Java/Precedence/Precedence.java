package Java.Precedence;

public class Precedence {
    public static void main(String[] args) {
        int x = 1, y = 2, z = 3;
        int a = x + y - 2 / 2 + z;
        int b = x + (y - 2) / (2 + z);
        //println()中的+可将元素转换为string并连接到前面的string中
        System.out.println("a = " + a);
        System.out.println("b = " + b);
    }
}
