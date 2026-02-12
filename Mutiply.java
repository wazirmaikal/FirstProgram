import java.util.Scanner;

public class Mutiply {
    public static void main(String[] args) {
       


   Scanner se=new Scanner(System.in);
   boolean done=false;
    do 
    {
    System.out.print("Select your shape \n1 for rectangle \n2 for right face triangle \n3 for left face triangle \n4 for isoselous triagle \n5 for number triangle \nEnter :    ");
    int num=se.nextInt();
        if( num==1)//rectangle 
        {
            for(int i=1;i<=4;i++){
                System.out.print("*");
                    for(int j=1;j<=10;j++){
                    System.out.print("*"); 
                   }
                   System.out.println("");
            }

        }
        else if(num==2)//right face triangle
        {
            for (int i = 1; i <=5; i++) 
            {
                for (int j= 1; j<=i; j++){
                    System.out.print("*");
                    
                }
            System.out.println("");
                   
            }

        }
        else if(num==3)//left face triangle
        {
            for (int i = 1; i <=5; i++) 
            {
                for (int j = 5; j >i; j--) 
                {
                    System.out.print(" ");
                }
                for (int z = 1; z <=i; z++) {
                   System.out.print("*"); 
                }
            System.out.println("");
            }

        }
      else if(num==4)// full triangle
      {
        for (int i = 1; i <=5; i++) 
        {
            for (int s = 5; s>i; s--){
                System.out.print(" ");
            }
        for (int z = 1; z <=2*i-1; z++) 
        {
            System.out.print("*");
            
        }
        System.out.println("");
        }
      }
      else if (num ==5) //number triangle
      { 
         for (int i = 1; i <=5; i++) 
        {
            for (int s = 5; s>i; s--){
                System.out.print(" ");
            }
        for (int z = 1; z <=2*i-1; z++) 
        {
            System.out.print(i);
            
        }
        System.out.println("");
        }
      }
      else {
      System.out.println("Invalid selection");}  

    System.out.println("Do you want to choose another shape \n Enter (y to yes) and )(n yo no) to cancel");
    char op=se.next().trim().charAt(0);
    op=Character.toLowerCase(op);
    if (op=='y') {
        done=true;
    }else if(op=='n'){
         done=false;
         System.out.println("\nTHANKYOU!\n");
    }
    }
    while (done) ;
  }     
}
    