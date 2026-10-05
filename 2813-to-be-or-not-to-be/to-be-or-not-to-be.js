
var expect = function(val) {

    return {

        toBe: function(x) {

            if (val === x) {
                return true;
            } else {
                throw new Error("Not Equal");
            }

        },

        notToBe: function(x) {

            if (val !== x) {
                return true;
            } else {
                throw new Error("Equal");
            }

        }

    };

};