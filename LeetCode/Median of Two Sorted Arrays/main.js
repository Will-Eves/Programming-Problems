/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let zip = [];

    let a = 0;
    let b = 0;
    for(let i = 0; i < nums1.length + nums2.length; i++){
        if(a == nums1.length){
            zip.push(nums2[b]);
            b++;
        }else if(b == nums2.length){
            zip.push(nums1[a]);
            a++;
        }else if(nums1[a] <= nums2[b]){
            zip.push(nums1[a]);
            a++;
        }else{
            zip.push(nums2[b]);
            b++;
        }
    }

    // return median of array
    let index = Math.floor((zip.length-1)/2);

    if(zip.length % 2 == 0){
        return (zip[index] + zip[index+1]) / 2;
    }else{
        return zip[index];
    }
};