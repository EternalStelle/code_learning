package Java.Assignment;

//创建Tank类，有属性level
class Tank {
    int level;
}

public class Assignment {
    public static void main(String[] args) {
        Tank t1 = new Tank();
        Tank t2 = new Tank();
        t1.level = 9;
        t2.level = 47;
        System.out.println("1: t1.level: " + t1.level + ", t2.level: " + t2.level);
        //此处即为引用，java自动清除了t1的原值，此时t1和t2的对象相同
        //若仅想赋值，可写t1.level=t2.level
        t1 = t2;
        System.out.println("2: t1.level: " + t1.level + ", t2.level: " + t2.level);
        //故更改t1实质上是更改t2，因此t1与t2的level值相同
        t1.level = 27;
        System.out.println("3: t1.level: " + t1.level + ", t2.level: " + t2.level);
    }
}
