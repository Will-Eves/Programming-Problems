/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let start_index = 0;
    let letters = '';
    let longest = 0;

    let i = 0;
    while(i < s.length){
        if(letters.indexOf(s[i]) != -1){
            if(letters.length > longest) longest = letters.length;
            letters = '';
            i = start_index;
            start_index = i+1;
        }else{
            letters += s[i];
        }

        i++;
    }

    if(letters.length > longest) longest = letters.length;

    return longest;
};