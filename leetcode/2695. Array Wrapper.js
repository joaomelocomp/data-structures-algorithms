var ArrayWrapper = function(nums) {
    this.nums = nums
};

ArrayWrapper.prototype.valueOf = function() {
    let soma = 0
    for (let i of this.nums) {
        soma += i
    }
    return soma
}

ArrayWrapper.prototype.toString = function() {
    return '[' + this.nums.join(',') + ']'
}
