
    
function Home(rooms, apartment, color, swimmingPool, state, city){
    this.rooms = rooms;
    this.apartment = apartment;
    this.color = color;
    this.swimmingPool = swimmingPool;
    this.state = state;
    this.city = city
};

function Book(numberOfPages, color, title, yearPublished){
    this.numberOfPages = numberOfPages;
    this.color = color;
    this.title = title;
    this.yearPublished = yearPublished;
};

const house = new Home(4,false,'red',true,'OK','Jenks');
const apartment = new Home(3,true,'white',false,'OK','Jenks')
const apartment2 = new Home(15,true,'green',true,'OK','tulsa')

    console.log(house)
    console.log(apartment)
    console.log(apartment2)

const Dictionary = new Book(1500,'black','The Dictionary of penis\'s', 2005)
const Arch = new Book(500,'Forest Green', 'ArchFunctions', 2012)
const Dicks = new Book(1200,'grey','The Dick Memior', 2105)
const Algerithyms = new Book(650,'red', 'Algerythmic Nonsense', 2016)
const Algerithyms2 = new Book(650,'red', 'Algerythmic Nonsense', 2016)

    console.log(Dictionary)
    console.log(Arch)
    console.log(Dicks)
    console.log(Algerithyms)
    console.log(Algerithyms2)

