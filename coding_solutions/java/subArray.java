public class subArray{
	public void subArray(int[] arrA){
	int arrSize=arrA.length;
	for(int i=0; i<arrSize; i++){
		for(int j=i;j<=arrSize; j++){
			for(int k=i; k<j; k++){
				System.out.print(arrA[k]+" ");
			}
			System.out.println();
		}
	}	
}	

public static void main(String[] args){
	int[]arrA={1,2,3,4};
	new subArray().subArray(arrA);
}
}