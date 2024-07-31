public class Main {
    public static void main(String args[])
    {
        int arr[]=new int[10];
        arr={0,1,1,2,0,1,2};
        int n=arr.length;
        int low,mid,high;
        low,mid=0;
        high=n-1;
        while(mid<=high)
        {
            for(int i=0;i<n;i++)
            {
                if(arr[mid]==0)
                {
                    low=low+mid;
                    mid=low-mid;
                    low=low-mid;
                    low++;
                    mid++;
                }
                if(arr[mid]==1)
                {
                    mid++;
                }
                if(arr[mid]==2)
                {
                    high=high+mid;
                    mid=high-mid;
                    high=high-mid;
                    high--;
                }
            }
        }
        for(int i=0;i<n;i++)
        {
            System.out.println(arr[i]+"\t");
        }
    }
    
}
