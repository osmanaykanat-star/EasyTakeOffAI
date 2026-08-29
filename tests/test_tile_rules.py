from backend.trades.tile_and_stone import TileAndStoneEngine

def test_tile_rules_calculation():
    items = TileAndStoneEngine.generate_room_items(
        floor_tile_symbol="TL-5",
        wall_tile_symbols=["TL-3.1", "TL-3.2"],
        wall_tile_percentages=[0.5, 0.5],
        floor_area_sqft=100.0,
        net_wall_area_sqft=200.0,
        perimeter_lnft=40.0,
        door_count=1,
        include_waterproofing=True,
        include_mudset=True,
        include_epoxy=True,
        include_saddle=True
    )
    
    symbols = {i.symbol: i.quantity for i in items}
    assert "TL-5" in symbols and symbols["TL-5"] == 100.0
    assert "SADDLE" in symbols and symbols["SADDLE"] == 1.0
    assert "TL-3.1" in symbols and symbols["TL-3.1"] == 100.0
    assert "TL-3.2" in symbols and symbols["TL-3.2"] == 100.0
    assert "WATERPROOF" in symbols and symbols["WATERPROOF"] == 100.0
    assert "MUDSET" in symbols and symbols["MUDSET"] == 100.0
    assert "EPOXY" in symbols and symbols["EPOXY"] == 300.0 # 100 floor + 200 wall
    
    print("test_tile_rules_calculation passed successfully!")

if __name__ == "__main__":
    test_tile_rules_calculation()
