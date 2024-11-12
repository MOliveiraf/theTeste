// Importa a função sevenSegmentify
const sevenSegmentify = require('./sevenSegmentify');

describe("sevenSegmentify", () => {
  it("should work on 13:24", () => {
    expect(sevenSegmentify("13:24")).toEqual(`
        _     _    
      | _| .  _||_|
      | _| . |_   |`.slice(1));
  });

  it("should work on 08:56", () => {
    expect(sevenSegmentify("08:56")).toEqual(`
       _     _  _ 
      |_| . |_ |_ 
      |_| .  _||_|`.slice(1));
  });

  it("should work on 00:00", () => {
    expect(sevenSegmentify("00:00")).toEqual(`
       _  _     _  _
      | || | . | || |
      |_||_|   |_||_|`.slice(1));
  });
});
