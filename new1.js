/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let arr = s.split(" ");
    let minValue = 1;
    let result = [];
    for (let i = 0; i < arr.length; i++) {
            if(minValue === Number(arr[i][arr[i].length-1])) {
                let removeArr = arr[i].split("");
                removeArr.splice(removeArr.length-1,1)
                result.push(removeArr.join(''));
                minValue++;
                arr.splice(i,1);
                i = -1;
            }
        
    }
    return result.join(' ');
};