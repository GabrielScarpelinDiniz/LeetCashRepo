func sortColors(nums []int)  {
    for i := 0;i<len(nums);i++{
        for j := 0; j < len(nums) - 1 - i; j++{
            if nums[j]>nums[j+1]{
                nums[j], nums[j+1] = nums[j+1], nums[j]
            }
        }
    }
}

Aplicacao de bubble sort bem simplesinha em go, vai comparando de duplas e em cada iteração deixa o o maior no final. No final de todas iterações o array estara ordenado. Bem suavinho.