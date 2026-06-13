var choice=prompt("Welcome to Area Calculator.\n Please Enter your Choice. \n1.Area of Rectangle. \n2. Area Of Triangle. \n3.Area Of Circle. \n4. Area Of Parallelogram.");

if (choice=='1'){

    var length =prompt('Enter the length')
    var breadth=prompt('Enter the breadth')

    var result=Number(length)*Number(breadth)
    alert('The area is'+ result)
}
if (choice=='1'){

    var length =prompt('Enter the length')
    var breadth=prompt('Enter the breadth')

    var result=Number(length)*Number(breadth)
    alert('The area is'+ result)
}
else if (choice == '2') {
    var base = prompt('Enter the base');
    var height = prompt('Enter the height');
    var result = 0.5 * Number(base) * Number(height);
    alert('The area of the triangle (base-height) is: ' + result);
}
else if(choice=='3'){
    var radius=prompt('Enter the Radius');
    var result=Math.PI*Math.pow(Number(radius), 2);
    alert('The area of the circle is '+result);
}
else if(choice=='4'){
    var base=prompt('Enter the base');
    var height=prompt('Enter the height');
    var result=Number(base)*Number(height);
    alert('The area of parallelogram is'+result);
}