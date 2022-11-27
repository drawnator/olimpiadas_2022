import java.util.Scanner;
public class Example{
  public static void main(String[] args) {
  Scanner sc = new Scanner(System.in);
  String entr[] = sc.nextLine().split(" ");
  int nums[] = new int[entr.length];
  for(int i=0;i<entr.length;i++){nums[i] = Integer.parseInt(entr[i]);}

  for (int num: nums ) {System.out.println(num);}
  }
}

  // String[] valsa = {"fornalha",
  // "fundidor",
  // "faunomante",
  // "gigante de ferro",
  // "pirata",
  // "pontifice"};
  // for (String identidades : valsa ) {System.out.println(identidades);}
  // System.out.println(valsa.length);

  // System.out.println(entr == "+");
  // switch (entr) {
  //   case "+":
  //     System.out.println("numero 1");
  //     break;
  //   case "-":
  //     System.out.println("numero 2");
  //     break;
  //   case "*":
  //     System.out.println("numero 3");
  //     break;
  //   default:
  //     System.out.println("numero 4");}
