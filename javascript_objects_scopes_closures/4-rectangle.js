#!/usr/bin/node

/* Exporting the class Rectangle. */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * For each row, print a string of X's that is equal to the width of the rectangle
   */
  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }

  /**
   * It swaps the width and height of the rectangle
   */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /**
  * This function doubles the width and height of the rectangle.
  */
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
