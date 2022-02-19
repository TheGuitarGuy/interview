function oddOneOut(nums)
{
    nums.sort();
    n = Math.max(nums)
    for(i = 0; i < n+1; i++)
    {
        if (i != nums[i])
        {
            return i
        }
    }
}
console.log(oddOneOut([1,3,2,0,5]))